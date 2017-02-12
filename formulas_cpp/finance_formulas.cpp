#include <cmath>
#include <boost/python.hpp>


double interest(double rate, int years)
{
    return pow(1 + rate, years);
}

double compound(double rate, int compound_amount, int years)
{
    double acutal_rate = rate / compound_amount;
    double result = pow(1 + acutal_rate, years * compound_amount);
    return result;
}

double continous_compound(double rate, int years)
{
    double rT = rate * years;
    return pow(M_E, rT);
}


BOOST_PYTHON_MODULE(finance_formulas)
{
    using namespace boost::python;
    def("interest", interest);
    def("compound", compound);
    def("continous_compound", continous_compound);
}
