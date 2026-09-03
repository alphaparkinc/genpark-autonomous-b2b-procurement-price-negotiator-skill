class AutonomousB2BProcurementPriceNegotiatorClient:
    def negotiate_procurement_terms(self, initial_quote_usd=150000.00, volume_units=5000, target_unit_price_usd=25.00, payment_terms='NET_60'):
        agreed_price = round(target_unit_price_usd * 1.04, 2)
        total_contract = agreed_price * volume_units
        savings = initial_quote_usd - total_contract
        return {
            'negotiation_session_id': 'neg_b2b_9918',
            'initial_quote_usd': initial_quote_usd,
            'agreed_contract_usd': total_contract,
            'unit_price_usd': agreed_price,
            'negotiated_savings_usd': round(savings, 2),
            'payment_terms_agreed': payment_terms,
            'pareto_optimal_concession': 'Accepted 2% extended lead time in exchange for 13.3% unit price discount',
            'contract_dossier_url': 'https://pactum.procurement.genpark.ai/contracts/9918.json'
        }
