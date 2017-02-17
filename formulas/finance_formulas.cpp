#include <cmath>
#include <vector>
#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>

using std::vector;


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

double annuity(vector<double>payments_per_year)
{
    double increase = 0;
    for (auto&& amount : payments_per_year) {
        increase += amount;
    }
    return increase;
}


BOOST_PYTHON_MODULE(finance_formulas)
{
    using namespace boost::python;
    class_<vector<double> >("double_vector")
                .def(vector_indexing_suite<vector<double> >() );
    def("interest", interest);
    def("compound", compound);
    def("continous_compound", continous_compound);
    def("annuity", annuity);
}
