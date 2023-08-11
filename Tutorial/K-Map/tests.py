#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Kmap import Minterms
from utils import Term


def test_result(
        str_terms = [6,8,10,11,12,13], 
        terms_not_care = [9, 14]
    ):
    
    str_terms = [str(format(a,'04b')) for a in str_terms]
    terms_not_care = [str(format(a,'04b')) for a in terms_not_care]
    
    t_minterms = [Term(term) for term in str_terms]
    terms_not_care = [Term(term) for term in terms_not_care]

    minterms = Minterms(t_minterms, terms_not_care)
    minterms.simplify()


if __name__ == "__main__":
    test_result()
