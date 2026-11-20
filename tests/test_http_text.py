"""Pages are decoded with their declared charset: Czech news sites still serve windows-1250."""
from dd.http import Resp


def _resp(body: bytes, ctype: str = "text/html") -> Resp:
    return Resp(url="https://example.cz", status=200, content=body, content_type=ctype, from_cache=False,
                sha256="", raw_path="")


def test_declared_and_undeclared_windows_1250():
    name = "Radomír Čech"
    assert _resp(name.encode("cp1250"), "text/html; charset=windows-1250").text == name
    meta = b'<html><head><meta charset="windows-1250"></head>' + name.encode("cp1250")
    assert name in _resp(meta).text
    assert _resp(name.encode("cp1250")).text == name          # nothing declared, not valid UTF-8
    assert _resp(name.encode("utf-8")).text == name
