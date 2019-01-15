import sys
import os
import decimal
import numbers

import logging
import logging.handlers as handlers
import time
from tkinter import Label,Button, Tk, HORIZONTAL ,messagebox
from tkinter.ttk import Progressbar
import threading

#from dbfread import DBF
from minor import Configure

from minor import AlohaDBF
from minor.model import DBF
from minor.dbfstore import dbf ,record

import json
import configparser

#Other sub class

# append module root directory to sys.path
sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)
"""
    [b'ID', b'OWNERID', b'USERNUMBER', b'SEC_NUM', b'SSN', b'SSNTEXT', b'FIRSTNAME', b'MIDDLENAME', b'LASTNAME', b'NICKNAME', b'ADDRESS1', b'ADDRESS2', b'CITY', b'STATE', b'ZIPCODE', b'PHONE', b'COUNTRY', b'COUNTRYCDE', b'LOCALEID', b'BIRTHDAY', b'DATEOFHIRE', b'LASTACCES
    S', b'PASSWORD', b'MAGCARD', b'SECURITY', b'TIPS', b'QWERTY', b'WKTOTMIN', b'WKTOVMIN', b'WKDOVMIN', b'WKTOTPAY', b'WKTOVPAY', b'WKDOVPAY', b'JOBCODE1', b'JOBCODE2', b'JOBCODE3', b'JOBCODE4', b'JOBCODE5', b'JOBCODE6', b'JOBCODE7', b'JOBCODE8', b'JOBCODE9', b'JOBCODE10
    ', b'PAYRATE1', b'PAYRATE2', b'PAYRATE3', b'PAYRATE4', b'PAYRATE5', b'PAYRATE6', b'PAYRATE7', b'PAYRATE8', b'PAYRATE9', b'PAYRATE10', b'ACCESS1', b'ACCESS2', b'ACCESS3', b'ACCESS4', b'ACCESS5', b'ACCESS6', b'ACCESS7', b'ACCESS8', b'ACCESS9', b'ACCESS10', b'SKILL1', b'
    SKILL2', b'SKILL3', b'SKILL4', b'SKILL5', b'SKILL6', b'SKILL7', b'SKILL8', b'SKILL9', b'SKILL10', b'PREF1', b'PREF2', b'PREF3', b'PREF4', b'PREF5', b'PREF6', b'PREF7', b'PREF8', b'PREF9', b'PREF10', b'MEALS', b'MEALPCNT', b'TERMINATED', b'ZAPID', b'REHIRE', b'LASTDAY'
    , b'RTNDAY', b'ZAPEXPLN', b'XFERUNIT', b'MOVE', b'MARITAL', b'NUMDEPEND', b'EXEMPT', b'WITHEXTRA', b'VETRANSTAT', b'MAGONLY', b'DDLRFEE', b'DPRCNTFEE', b'DMLGFEE', b'DDLEXP', b'DINSRNCEXP', b'SEX', b'JOBSTATUS', b'EMPCODE1', b'EMPCODE2', b'BOHPASSWRD', b'SECLEVEL', b'
    STARTTIME', b'ENDTIME', b'PWDCHANGE', b'PENID', b'TEAMSORT', b'TEAMLMTREV', b'ADDRESS3', b'ADDRESS4', b'COUNTY', b'THUMBSCCI', b'WORKPOLID', b'EMPTYPEID', b'THUMBSCLI', b'REMARKS', b'SCHEDSTART', b'SCHEDEND', b'EMPCODE3', b'EMPCODE4', b'EMPCODE5', b'WAIVEMBRK', b'LAST
    CHPSWD', b'BOHLASTPWD', b'NCFLOGON', b'SSN_ENC', b'EMPLIQCERT', b'EMPLIQEXP', b'MINORXMT', b'BOHHASHPW', b'EXP_ID']
"""
JOBCODE = ['JOBCODE1', 'JOBCODE2', 'JOBCODE3', 'JOBCODE4', 'JOBCODE5', 'JOBCODE6', 'JOBCODE7', 'JOBCODE8','JOBCODE9', 'JOBCODE10']
PAYRATE = ['PAYRATE1', 'PAYRATE2', 'PAYRATE3', 'PAYRATE4', 'PAYRATE5', 'PAYRATE6', 'PAYRATE7', 'PAYRATE8','PAYRATE9', 'PAYRATE10']
ACCESS  = ['ACCESS1', 'ACCESS2', 'ACCESS3', 'ACCESS4', 'ACCESS5', 'ACCESS6', 'ACCESS7', 'ACCESS8', 'ACCESS9','ACCESS10']
DBF_FILE = {"EMP":"EMP.DBF"}
CREATED_ROWS = []


def log(message):
    Configure.logger.info(str(message))


if __name__ == "__main__":
    hasNewRecordCreated = False
    try:
        log("############# Start Running")
        log("Load configuration file config.ini")
        config = Configure.ConfigureData("config.ini")

        site_number = config.ConfigSectionMap("Minor")['site_number']
        menulink_ver = float(config.ConfigSectionMap("MenuLink")['version'])
        aloha_ver = float(config.ConfigSectionMap("Aloha")['version'])
        log("MunuLink version " + str(menulink_ver))
        log("Aloha version " + str(aloha_ver))

        newdata_location = config.ConfigSectionMap("Aloha")['newdata_path']


    except FileNotFoundError:
        log("The DBF File is not found")
        raise SystemExit("The DBF File is not found")

    log("Finished")
print("aha aha")



