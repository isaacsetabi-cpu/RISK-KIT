#ifndef __FinancialSamples__CompoundIntRateCalculator__
#define __FinancialSamples__CompoundIntRateCalculator__

class CompoundIntRateCalculator{
	public:
		CompoundIntRateCalculator(double rate); // constructor
		CompoundIntRateCalculator(const CompoundIntRateCalculator &v);
		CompoundIntRateCalculator &operator = (const CompoundIntRateCalculator &v);
		~CompoundIntRateCalculator();
		
		double multiplePeriod(double value, int numPeriod);
		double continuousCompounding(double value, int numPeriod);
	private:
		double m_rate;	
};
#endif


