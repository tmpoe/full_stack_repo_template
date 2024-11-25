
import nox
from nox.sessions import Session


@nox.session(python="3.12", reuse_venv=True)
def lint(session: Session) -> None:
    session.run("python", "--version")
    # session.run("pip", "install", "--upgrade", "pip")
    # session.install("poetry")
