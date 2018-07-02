#!/usr/bin/env python
import pytest
import agave
import requests


def test_hello_parser(capfd):
    args = agave.parser.parse_args(["hello", "--greeting", "hi", "john"])
    args.func(args)
    out, err = capfd.readouterr()
    assert out == "hi, john!\n"
    assert err == ""


def test_hello_parser_caps(capfd):
    args = agave.parser.parse_args(["hello", "-c", "-g", "Hola", "john"])
    args.func(args)
    out, err = capfd.readouterr()
    assert out == "HOLA, JOHN!\n"
    assert err == ""


def test_tenant_ls(capfd):
    args = agave.parser.parse_args(["tenant", "ls"])
    args.func(args)
    out, err = capfd.readouterr()
    assert "CODE                 NAME" in out
    assert err == ""


def test_tenant_ls_Herr(capfd):
    with pytest.raises(SystemExit) as e:
        args = agave.parser.parse_args(["tenant", "ls", "-H", "http"])
        args.func(args)
        out, err = capfd.readouterr()
        assert "CODE                 NAME" in out
        assert err == "Invalid URL 'http': No schema supplied. Perhaps you meant http://http?\n"
        assert e.type == SystemExit
        assert e.value.code == 1
