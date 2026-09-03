from client import AutonomousB2BProcurementPriceNegotiatorClient

def main():
    client = AutonomousB2BProcurementPriceNegotiatorClient()
    res = client.negotiate_procurement_terms(200000.00, 10000, 18.00)
    print('B2B Procurement Negotiator: ' + res['negotiation_session_id'])
    print('Agreed Contract: $' + str(res['agreed_contract_usd']) + ' (Saved: $' + str(res['negotiated_savings_usd']) + ')')
    print('Dossier URL: ' + res['contract_dossier_url'])

if __name__ == '__main__':
    main()
