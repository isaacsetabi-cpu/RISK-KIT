#include "cashFlowCalculator.h"
#include<iostream>
#include<cstdlib>
#include<cmath>

cashFlowCalculator::cashFlowCalculator(double rate):m_rate(rate){
	
}

cashFlowCalculator::cashFlowCalculator(const cashFlowCalculator &v):m_rate(v.m_rate){
	
}

cashFlowCalculator::~cashFlowCalculator(){
}

cashFlowCalculator &cashFlowCalculator::operator=(const cashFlowCalculator &v)
{
	if(this != &v){
		this->m_cashPayments = v.m_cashPayments;
		this->m_timePeriod = v.m_timePeriod;
		this->m_rate = v.m_rate;
	} 
	return *this;
}

void cashFlowCalculator::addCashPayment(double value, int timePeriod)
{
	m_cashPayments.push_back(value);
	m_timePeriod.push_back(timePeriod);
}

double cashFlowCalculator::presentValue(double futureValue, int timePeriod)
{
	double pValue = futureValue / pow(1+m_rate, timePeriod);
	std::cout << "value" << pValue <<std::endl;
	return pValue;
 } 
 
 double cashFlowCalculator::presentValue(){
 	double total = 0;
	for(int i=0; i<m_cashPayments.size(); ++i){
		total += presentValue(m_cashPayments[i], m_timePeriod[i]);
	}
	return total;
}
