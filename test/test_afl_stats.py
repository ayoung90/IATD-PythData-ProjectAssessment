import pytest
from testbook import testbook
import pdb

# https://seleniumbase.com/the-ultimate-pytest-debugging-guide-2021/

@pytest.fixture(scope='module')
def tb():
    with testbook('afl_stats.ipynb', execute=True) as tb:
        yield tb

#verify that all csvs were loaded and contain data
def test_csv_load(tb):
    """ Validate that all files load successfully 
    Args:
        tb (testbook): afl_stats jupyter notebook
    """
    
    stats_ref = tb.ref("stats")
    players_ref = tb.ref("players")
    games_ref = tb.ref("games")

    #validate files are not empty
    assert len(stats_ref) > 0
    assert len(players_ref) > 0
    assert len(games_ref) > 0

    stats_ref2 = tb.value("stats['gameId'][0]")
    
    #init trace
    #pdb.set_trace()
    
    assert type(stats_ref2) == str
    
def test_games_stats_players_columns(tb):
    """ validates that one column from each file exists in joined dataframe
    Args:
        tb (testbook): afl_stats jupyter notebook
    """
    
    #extract all keys from joined dataframe
    key_columns = tb.value("games_stats_players.keys().array.tolist()")
    
    #check at least 1 column exists from each file
    assert key_columns.__contains__("venue") #games
    assert key_columns.__contains__("height") #players
    assert key_columns.__contains__("Handballs") #stats