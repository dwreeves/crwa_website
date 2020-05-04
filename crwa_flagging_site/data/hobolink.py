"""
This file handles connections to the HOBOlink API, including cleaning and
formatting of the data that we receive from it.
"""

import pandas as pd
import requests
import io
from .keys import load_keys, HTTPException

# TODO:
#  Pandas is inefficient. It should go to SQL, not to Pandas. I am currently
#  using pandas because we do not have any cron jobs or any caching or SQL, but
#  I think in future versions we should not be using Pandas at all.

# Constants
# ~~~~~~~~~

HOBOLINK_URL = 'http://webservice.hobolink.com/restv2/data/custom/file'
EXPORT_NAME = 'code_for_boston_export'

# ~ ~ ~ ~


def get_hobolink_data(export_name: str = EXPORT_NAME) -> pd.DataFrame:
    """
    This function runs through the whole process for retrieving data from
    HOBOlink: first we perform the request, and then we clean the data.

    :param export_name: Name of the "export." On the Hobolink web dashboard, go
                        to Data > Exports and choose a name off the list.
    :return: Pandas DataFrame containing HOBOlink data.
    """
    res = request_to_hobolink(export_name=export_name)
    df = parse_hobolink_data(res.text)
    return df


def request_to_hobolink(
        export_name: str = EXPORT_NAME
) -> requests.models.Response:
    """
    Get a request from the Hobolink server.

    :param export_name: Name of the "export." On the Hobolink web dashboard, go
                        to Data > Exports and choose a name off the list.
    :return: Request Response containing the data from the request.
    """
    auth = load_keys()['hobolink']
    data = {
        'query': export_name,
        'authentication': auth
    }
    res = requests.post(HOBOLINK_URL, json=data)
    if res.status_code // 100 in [4, 5]:
        raise HTTPException(res.text)
    return res


def parse_hobolink_data(res: str) -> pd.DataFrame:
    """
    Clean the response from the API.

    :param res: A string of the text received from the post request to the
                HOBOlink API from a successful request.
    :return: Pandas DataFrame containing HOBOlink data.
    """
    if isinstance(res, requests.models.Response):
        res = res.text
    split_by = '------------'
    str_table = res[res.find(split_by) + len(split_by):]
    df = pd.read_csv(io.StringIO(str_table), sep=',')
    # TODO:
    #  Make column names nicer to work with
    return df
