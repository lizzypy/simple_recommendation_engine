import pandas as pd
import pytest


@pytest.fixture
def expected_movies_dataframe():
    data = [[588, "Aladdin (1992)", "adventure|animation|children|comedy|musical|fantasy"],
            [114240, "Aladdin (1992)", "adventure|animation|children|comedy|musical|fantasy"],
            [356, "Forrest Gump (1994)", "comedy|drama|romance|war|action"],
            [1236, "Forrest Gump (1994)", "comedy|drama|romance|war|action"],
            [1, "Toy Story (1995)", "adventure|animation|children|comedy|fantasy"]]
    return pd.DataFrame(data, columns=['movieId', 'title', 'genres'])
