import nox

nox.options.sessions = ["test"]
nox.options.reuse_existing_virtualenvs = True

TINYURL_MODULES = (
    "shortner",
)


tinyurl_module_paramater = nox.parametrize(
    "tinyurl_module", TINYURL_MODULES, ids=TINYURL_MODULES
)


@nox.session(python=["3.8"])
@tinyurl_module_paramater
def test(session, tinyurl_module):
    """ Run the tests """
    session.install("-r", "requirements.txt")
    directory = f"{tinyurl_module}"
    session.cd(directory)
    command = ["pytest", "--cov={}".format(tinyurl_module)]
    session.run(*command)