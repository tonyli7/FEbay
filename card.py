from database import *
import sqlite3

def add_credit_card(card, email):
    conn = sqlite3.connect('cse305.db')
    c = conn.cursor()
    success = True
    userID = get_userid(email)
    try:
        c.execute('''
        INSERT INTO CreditCard(UserID, CCN, SecurityCode, ExpiryDate) VALUES ({}, {}, {}, '{}')
        '''.format(userID, card['ccn'], card['securitycode'], card['expirydate']))
        conn.commit()
    except sqlite3.Error as e:
        print("Database error: %s" % e)
        conn.rollback()
        success = False
    finally:
        conn.close()
        return success

def remove_credit_card(card, email):
    conn = sqlite3.connect('cse305.db')
    c = conn.cursor()
    success = True
    userID = get_userid(email)
    try:
        c.execute('''
        DELETE FROM CreditCard
        WHERE CCN = {} AND UserID = {}
        '''.format(card['ccn'], userID))
        conn.commit()
    except sqlite3.Error as e:
        print("Database error: %s" % e)
        conn.rollback()
        success = False
    finally:
        conn.close()
        return success

def update_credit_card(card, email):
    conn = sqlite3.connect('cse305.db')
    c = conn.cursor()
    success = True
    userID = get_userid(email)
    try:
        c.execute('''
        UPDATE CreditCard
        SET CCN = {}, SecurityCode = {}, ExpiryDate = '{}'
        WHERE CCN = {} AND UserID = {}
        '''.format(card['ccn'], card['securitycode'], card['expirydate'], card['original'], userID))
        conn.commit()
    except sqlite3.Error as e:
        print("Database error: %s" % e)
        conn.rollback()
        success = False
    finally:
        conn.close()
        return success

def get_cards():
    conn = sqlite3.connect('cse305.db')
    c = conn.cursor()
    c.execute('''
    SELECT * FROM CreditCard
    ''')
    rows = c.fetchall()
    cards = []
    for row in rows:
        cards.append({'UserID':row[0],'CCN':row[1],'SecurityCode':row[2],'ExpiryDate':row[3]})
    conn.close()
    return cards
