===========================================================
challongebot - an IRC tournament bot for Challonge brackets
===========================================================


Requirements
============

* `pychallonge <http://github.com/russ-/pychallonge>`_
* `willie <http://willie.dftba.net/>`_
* A Challonge API key

Note that depending on ``willie`` requires Python 2.7 or higher to be used, as well. ``pychallonge`` also requires `dateutil <http://labix.org/python-dateutil>`_ be installed, as well.


Installation
============

``challongebot`` is a ``willie`` module, so copy it to your ``willie`` module directory, which will typically be located in ``C:\Python27\Libs\site-packages\willie\modules`` on Windows, or ``/usr/local/lib/python2.7/dist-packages/willie/`` on Linux. See the willie documentation for more info on how to install modules like challongebot.

Be sure to modify the ``CHALLONGE_USERNAME``, ``TOURNAMENT_NAME``, and ``API_KEY`` variables in ``challongebot.py`` before installing it.


Running challongebot
====================

* Start up ``willie as per normal. See the ``willie`` documentation for more on this.
* Type ``.setup`` to initialize ``challongebot``.
* Use the ``.update`` command to have ``challongebot`` update the brackets.


Commands
========

**.setup**

Initializes ``challongebot``. The command must be issued by the ``willie`` instance's owner to work.

**.pending**

Lists all matches which are waiting for results.

**.update MATCH_CODE PLAYER1_SCORE PLAYER2_SCORE**

Updates the results of an individual match. ``MATCH_CODE`` is the name of the match on Challonge, and PLAYER1_SCORE and PLAYER2_SCORE represent the scores of the two players - ``challongebot`` automatically detects the match winner based on these scores.
