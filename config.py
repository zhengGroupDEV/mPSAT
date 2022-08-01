from dynaconf import Dynaconf

msettings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.json", ".secrets.json"],
    environments=True,
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
