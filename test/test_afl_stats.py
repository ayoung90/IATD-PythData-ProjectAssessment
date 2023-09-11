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

#### TASK 1 - LOAD YOUR DATA ####
    
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

#TODO Any futher tests for task 1 ??

#### TASK 2 - PLOT ONE PLAYER ####
    
def test_cum_column(tb):
    """Checks that the "Goals (Cumulative)" is added to player_stats_desc

    Args:
        tb (testbook): afl_stats jupyter notebook
    """
    #TODO Implement test :)
    
#TODO Any futher tests for task 2 ??    
    
#### TASK 3 - PLOT MULTIPLE PLAYERS ####

def test_players_masks(tb):
    """Checks that the masks filter only to the specifed player

    Args:
        tb (testbook): afl_stats jupyter notebook
    """
    
    #TODO Implement test :)
    
def test_players_cum_columns(tb):
    """Checks that the "Goals (Cumulative)" column is added to all dataframes

    Args:
        tb (testbook): afl_stats jupyter notebook
    """   
    
    #TODO Implement test :)
    
def test_graph_attributes(tb):
    """Checks that the graphs x & y labels are correct?

    Args:
        tb (testbook): afl_stats jupyter notebook
    """
    
    #TODO Implement test :)        

#TODO Any futher tests for task 3 ??    

#### TASK 4 - LINEAR REGRESSION ####

#TODO Tests for task 4
    