"""
Description: infer
Author: Rainyl
Date: 2022-06-26 17:31:38
LastEditTime: 2022-06-27 20:40:02
"""
import pickle
from typing import List, Union

import numpy as np
import onnxruntime as ort
from PIL import Image
from scipy import sparse
from sklearn.tree import DecisionTreeClassifier
import sklearn.svm as svm
from sklearn.ensemble import RandomForestClassifier
from argparse import ArgumentParser

from mPSAT.utils.infer_base import MpInferenceBase


class MpInferenceSKL(MpInferenceBase):
    model: Union[DecisionTreeClassifier, svm.LinearSVC, RandomForestClassifier]

    def __init__(self, model_path: str, label_name: str):
        super(MpInferenceSKL, self).__init__(model_path, label_name)

    def load_model(self, p: str):
        with open(p, "rb") as f:
            model = pickle.load(f)
        return model

    def preprocess(self, imgs: Union[Image.Image, List[Image.Image]]):
        if not isinstance(imgs, list):
            imgs = [imgs]
        # dtype is important. trained with uint8, here it must be uint8
        x = [np.asarray(im, dtype=np.uint8).flatten() - 255 for im in imgs]
        x = sparse.csr_matrix(x)
        return x

    def __call__(self, img: List[Image.Image], topk=1) -> List[List[Union[int, str]]]:
        x = self.preprocess(imgs=img)
        # out = self.model.predict(x)
        proba: np.ndarray
        if isinstance(self.model, svm.LinearSVC):
            proba = self.model.decision_function(x)
        else:
            proba = self.model.predict_proba(x)
        # out_prob = self.softmax(proba, axis=1)
        out_prob = proba.copy()
        out_topk = out_prob.argsort(axis=1)[:, ::-1][:, :topk]
        out1 = self.label2name(out_topk.tolist())  # (N, topk)
        out2 = [out_prob[i][out_topk[i]] for i in range(out_topk.shape[0])]  # (N, topk)
        out3 = [  # (N, topk, 2)
            [out1[i][j], out2[i][j]]
            for i in range(len(out1))
            for j in range(len(out1[0]))
        ]
        return out3


# =================================================================
# for now, skl2onnx and onnxruntime don't support sparse matrix
# so, this method is not avaliable until they support or re-train
# model with normal matrix
# 2022.07.01
# =================================================================
class MpInferenceSKLONNX(MpInferenceBase):
    def __init__(self, model_path: str, label_name: str = "data/label_name.json"):
        raise NotImplementedError(f"for now, skl2onnx and onnxruntime don't support sparse matrix")
        super(MpInferenceSKLONNX, self).__init__(model_path, label_name)

    def load_model(self, p: str):
        sess = ort.InferenceSession(p)
        return sess

    def preprocess(self, imgs: Union[Image.Image, List[Image.Image]]):
        if not isinstance(imgs, list):
            imgs = [imgs]
        x = [np.asarray(im, dtype=np.float32).flatten() - 255.0 for im in imgs]
        # x = [sparse.csr_matrix(i) for i in x]
        # x = sparse.csr_matrix(x)
        return x

    def __call__(self, img: List[Image.Image]) -> List[List[Union[int, str]]]:
        x = self.preprocess(imgs=img)
        input_name = self.model.get_inputs()[0].name
        label_name = self.model.get_outputs()[0].name
        inputs = {input_name: x}
        out = self.model.run(None, inputs)[0]
        # out = out.argsort(dim=-1, descending=True)[:, :topk]
        out = self.label2name(out)
        return out


def main(img: str):
    # inferer = MpInferenceSKL("repeatSave/svmSave/1/clfLinearSVC.onnx")
    # inferer = MpInferenceSKL("repeatSave/svmSave/1/clfLinearSVC.pkl")
    inferer = MpInferenceSKL("repeatSave/rfSave/1/clfRF.pkl")
    # inferer = MpInferenceSKL("repeatSave/dtSave/1/clfDT.pkl")
    if img.endswith(".jpg"):
        im = Image.open(img).convert("L")
    elif img.endswith(".csv"):
        im = inferer.read_plot_csv(img, rmco2=True, fac=0.2)
    else:
        raise NotImplementedError(f"image format {img.split('.')[-1]} not implemented!")
    im.save(img+".jpg")
    out = inferer([im], topk=3)
    print([["+".join(c) for c in row] for row in out])  # type:ignore


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-i", dest="image", type=str)
    args = parser.parse_args()
    # args = parser.parse_args(
    #     ["-i", "data/dataset2206/dataset/datasetSplit430/test/0/129.13.jpg"]
    # )
    main(args.image)
