#!/usr/bin/env python
import pytest
import agave


def test_hello_parser(capfd):
    args = agave.parser.parse_args(["hello", "--greeting", "hi", "john"])
    args.func(args)
    out, err = capfd.readouterr()
    assert out == "hi, john!\n"
    assert err == ""


def test_hello_parser_caps(capfd):
    args = agave.parser.parse_args(
        ["hello", "-c", "-g", "Hola", "john"])
    args.func(args)
    out, err = capfd.readouterr()
    assert out == "HOLA, JOHN!\n"
    assert err == ""


def test_goodbye_parser(capfd):
    args = agave.parser.parse_args(["goodbye", "--greeting", "see ya", "john"])
    args.func(args)
    out, err = capfd.readouterr()
    assert out == "see ya, john!\n"
    assert err == ""


def test_goodbye_parser_caps(capfd):
    args = agave.parser.parse_args(
        ["goodbye", "--caps", "-g", "bai", "john"])
    args.func(args)
    out, err = capfd.readouterr()
    assert out == "BAI, JOHN!\n"
    assert err == ""
