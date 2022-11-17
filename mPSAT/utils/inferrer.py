"""
Description: Universal inference of ONNX models
Author: rainyl
License: Apache License 2.0
"""
import os
import random
from io import BytesIO
from typing import Dict, List, Union

import numpy as np
import onnxruntime as ort
from numpy.typing import NDArray
from PIL import Image, ImageChops

from .infer_base import MpInferenceBase


def seed_everything(seed: int):
    # from kaggle, https://www.kaggle.com/code/rhythmcam/random-seed-everything
    os.environ["PYTHONHASHSEED"] = str(seed)
    random.seed(seed)
    np.random.seed(seed)


class MpInferenceOnnx(MpInferenceBase):
    model: ort.InferenceSession
    __supported_models__ = ("dt", "rf", "cnn", "cnn2d")

    def __init__(
        self,
        model_path: str,
        model_name: str = "cnn",
        label_name: str = "data/label_name.json",
        device: str = "cpu",
    ):
        _providers = [
            (
                "CUDAExecutionProvider",
                {
                    "device_id": 0,
                    "arena_extend_strategy": "kNextPowerOfTwo",
                    "gpu_mem_limit": 2 * 1024 * 1024 * 1024,
                    "cudnn_conv_algo_search": "EXHAUSTIVE",
                    "do_copy_in_default_stream": True,
                },
            ),
            ("CPUExecutionProvider",),
        ]
        if device == "cpu":
            self.providers = _providers[1]
        elif device == "cuda":
            self.providers = _providers
        else:
            raise ValueError(f"device {device} not supported")
        super(MpInferenceOnnx, self).__init__(model_path, model_name, label_name)

    def load_model(self, p: str):
        sess = ort.InferenceSession(p, providers=self.providers)
        return sess

    def crop_bbox(self, img: Image.Image):
        bg = Image.new(img.mode, img.size, "white")
        diff = ImageChops.difference(img, bg)
        # diff = ImageChops.add(diff, diff)
        img = img.crop(diff.getbbox())
        return img

    def plot_fig(self, y: NDArray[np.float32]):
        # y: (B, 3600)
        import matplotlib
        import matplotlib.pyplot as plt

        matplotlib.use("Agg")
        # rng = np.random.default_rng()
        # lw = rng.uniform(0.1, 3)
        # figsize = (rng.integers(4, 10), rng.integers(4, 10))
        # plt.figure(figsize=(rng.integers(1, 10), rng.integers(1, 10)), dpi=rng.integers)
        figsize = (5, 5)
        lw = 1
        all_images = []
        for yy in y:
            plt.figure(figsize=figsize, dpi=120)
            plt.plot(self.xx, self.minmax(yy), lw=lw, color="k")
            plt.tight_layout()
            plt.axis("off")
            plt.xlim(4000, 400)
            plt.ylim(-0.01, 1)

            im_stream = BytesIO()
            plt.savefig(im_stream, bbox_inches="tight")
            im = Image.open(im_stream).convert("L")
            all_images.append(im)
            plt.clf()
            plt.close("all")

        return all_images

    def preprocess(self, spec: List[NDArray[np.float32]]):
        x = super().preprocess(spec)
        if self.model_name == "cnn":
            x = np.expand_dims(x, 1)
        elif self.model_name == "cnn2d":
            imgs = self.plot_fig(x)
            # (B, 1, H, W)
            imgs = [self.crop_bbox(im) for im in imgs]
            imgs = [im.resize((480, 480), Image.Resampling.LANCZOS) for im in imgs]
            x = np.asarray(
                [
                    np.expand_dims(
                        np.asarray(im, dtype=np.float32),  # (H, W)
                        0,
                    )
                    for im in imgs
                ],
                dtype=np.float32,
            )
        elif self.model_name in ["dt", "rf"]:
            ...
        else:
            raise ValueError()
        return x

    def __call__(
        self,
        spec: List[NDArray[np.float32]],
        topk: int = 3,
    ):
        x = self.preprocess(spec)
        input_name = self.model.get_inputs()[0].name
        inputs = {input_name: x}
        if self.model_name in ("cnn", "cnn2d"):
            out: NDArray[np.float32] = self.model.run(None, inputs)[0]
            out = self.softmax(out, axis=1)
        else:
            out: NDArray[np.float32] = self.model.run(None, inputs)[1]
        out_topk = out.argsort(axis=1)[:, ::-1][:, :topk]  # (N, topk)
        out1 = self.label2name(out_topk.tolist())  # (N, topk)
        out2 = [out[i][out_topk[i]] for i in range(out_topk.shape[0])]  # (N, topk)
        out3 = [  # (N, topk, 2)
            [out1[i][j], out2[i][j]]
            for i in range(len(out1))
            for j in range(len(out1[0]))
        ]
        return out3


if __name__ == "__main__":
    ...
