#!/usr/bin/env python
import pytest
import agave
import requests


def test_tenant_ls(capfd):
    args = agave.main_parser.parse_args(["tenant", "ls"])
    args.func(args)
    out, err = capfd.readouterr()
    assert "CODE                 NAME" in out
    assert err == ""


def test_tenant_ls_Herr(capfd):
    with pytest.raises(SystemExit) as e:
        args = agave.main_parser.parse_args(["tenant", "ls", "-H", "http"])
        args.func(args)
        out, err = capfd.readouterr()
        assert "CODE                 NAME" in out
        assert err == "Invalid URL 'http': No schema supplied. Perhaps you meant http://http?\n"
        assert e.type == SystemExit
        assert e.value.code == 1
