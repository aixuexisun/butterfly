"""Versions and header."""
from datetime import datetime


class Version(object):
    """Version class."""

    BFVer = "0.0.2"
    OFVer = "3.0"
    OFFullVer = "v1606+"
    isUsingDockerMachine = True  # useful to run OpenFOAM container
    lastUpdated = datetime(year=2016, month=9, day=29, hour=14, minute=00)


class Header(object):
    """
    Input files header.

    Usage:
        Header.header()
    """

    @staticmethod
    def header(OpenFOAMVersion=Version.OFFullVer, ButterflyVersion=Version.BFVer):
        """Retuen OpenFOAM file header."""
        header = "/*--------------------------------*- C++ -*----------------------------------*\\\n" + \
                 "| =========                 |                                                 |\n" + \
                 "| \\\\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n" + \
                 "|  \\\\    /   O peration     | Version:  {}                                 |\n" + \
                 "|   \\\\  /    A nd           | Web:      www.OpenFOAM.org                      |\n" + \
                 "|    \\\\/     M anipulation  |                                                 |\n" + \
                 "\\*---------------------------------------------------------------------------*/\n" + \
                 "/*Generated by Butterfly {} https://github.com/mostaphaRoudsari/Butterfly *\\\n" + \
                 "\\*---------------------------------------------------------------------------*/\n"

        return header.format(OpenFOAMVersion, ButterflyVersion)
