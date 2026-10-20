#ifndef __FinancialSamples__CashFlowCalculator__
#define __FinancialSamples__CashFlowCalculator__

#include<iostream>
#include<cstdlib>

class cashFlowCalculator{
	public:
		cashFlowCalculator(double rate);
		cashFlowCalculator(const cashFlowCalculator &v);
		cashFlowCalculator &operator = (const cashFlowCalculator &v);
		~cashFlowCalculator();
		
		void addCashPayment(double value, int timePeriod);
		double presentValue();
	
	private:
		std::vector<double> m_cashPayments;
		std::vector<int> m_timePeriod;
		double m_rate;
		double presentValue(double futureValue, int timePeriod);	
};
#endif


