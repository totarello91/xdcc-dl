"""
LICENSE:
Copyright 2016 Hermann Krumrey

This file is part of xdcc_dl.

    xdcc_dl is a program that allows downloading files via hte XDCC
    protocol via file serving bots on IRC networks.

    xdcc_dl is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    xdcc_dl is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with xdcc_dl.  If not, see <http://www.gnu.org/licenses/>.
LICENSE
"""

# imports
import argparse


def main() -> None:
    """
    Starts the main method of the program

    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--message", help="An XDCC Message")
    parser.add_argument("-s", "--server", help="Specifies the IRC Server. Defaults to irc.rizon.net")
    args = parser.parse_args()


if __name__ == "__main__":
    main()
