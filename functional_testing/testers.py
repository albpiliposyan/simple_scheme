import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(1, '../src/')
import interpreter as inter
import parsing


def tester(expression, expected_result):
    expr = parsing.tokenize(expression)
    expr = parsing.parenthesize(expr)
    result = inter.evaluate(expr)
    if inter.evaluate(expr) == expected_result:
        print('PASS: from', expression, 'got', result)
    else:
        print('FAIL: expected to get', expected_result, 'but got', result)


def test_op_add():
    tester('(+ 1 2 4)', 7)
    tester('(+ 0)', 0)
    tester('(+ 5 5 5 5 5)', 25)
    tester('(+ 1 2 3 (+ 1 2 3))', 12)


def test_op_sub():
    tester('(- 10 2 2)', 6)
    tester('(- 0)', 0)
    tester('(- 5 5 5 5)', -10)
    tester('(- 10 2 2 (- 0 2))', 8)


def test_op_mul():
    tester('(* 2 2 4)', 16)
    tester('(* 5)', 5)
    tester('(* -4 2 1)', -8)
    tester('(* -4 0)', 0)
    tester('(* 1 2 2 (* 1 3))', 12)


def test_op_truediv():
    tester('(/ 10 2)', 5)
    tester('(/ 1 5 5)', 1 / 25)
    tester('(/ 5)', 5)
    tester('(/ 12  2 (/ 6 2))', 2)


def test_op_gt():
    tester('(> 4 0)', True)
    tester('(> -4 0)', False)
    tester('(> 4 4)', False)


def test_op_lt():
    tester('(< 4 0)', False)
    tester('(< -4 0)', True)
    tester('(< 4 4)', False)


def test_op_ge():
    tester('(>= 4 0)', True)
    tester('(>= -4 4)', False)
    tester('(>= 4 4)', True)


def test_op_le():
    tester('(<= 4 0)', False)
    tester('(<= -4 4)', True)
    tester('(<= 4 4)', True)


def test_op_eq():
    tester('(= 4 4)', True)
    tester('(= -4 -4)', True)
    tester('(= 0 7)', False)


def test_eq_ref_ch():
    tester('(eq? 4 4)', True)


def test_equal_ch():
    tester('(equal? 4 4)', True)


def test_op_abs():
    tester('(abs 10)', 10)
    tester('(abs -10)', 10)


def test_max_f():
    tester('(max 1 2 5 4 3)', 5)
    tester('(max -1 -2 0 -4 -3)', 0)


def test_min_f():
    tester('(min 1 2 5 4 3)', 1)
    tester('(min -1 -2 0 -4 -3)', -4)


def test_and_f():
    tester('(and #t #f)', False)
    tester('(and #t #t)', True)
    tester('(and #t #f #t #t)', False)


def test_or_f():
    tester('(or #t #f)', True)
    tester('(or #f #f)', False)
    tester('(or #f #f #t #f)', True)


def test_not_f():
    tester('(not #t)', False)
    tester('(not #f)', True)


def test_number_ch():
    tester('(number? a)', False)
    tester('(number? 5)', True)
    tester('(number? #t)', True)


def test_symbol_ch():
    tester('(symbol? a)', True)
    tester('(symbol? 5)', False)
    tester('(symbol? #t)', False)


def test_null_ch():
    tester('(null? a)', False)
    tester('(null? 5)', False)
    tester('(null? #t)', False)


def test_list_ch():
    tester('(list? (list 1 2 3))', True)
    tester('(list? "aaaa")', False)


def test_round_f():
    tester('(round 12.64)', 13)
    tester('(round 12.12)', 12)
    tester('(round 12)', 12)


def test_remainder_f():
    tester('(remainder 5 3)', 2)
    tester('(remainder 2 3)', 2)
    tester('(remainder 5 5)', 0)
    tester('(remainder 25 5)', 0)
    tester('(remainder -11 5)', 4)


def test_string_append_f():
    tester('(string-append aaa bbb)', "aaa bbb")
    tester('(string-append 111 bbb)', "111 bbb")


def test_display():
    tester('(display sentence)', "sentence")
    tester('(display "A test sentence")', "A test sentence")
    tester('(display sentence)', "sentence")


def test_newline():
    tester('(newline)', "\n")


def test_if_f():
    tester('(if (< 0 1) "Zero is less than one" "Zero is not less than one")',
           '"Zero is less than one"')
    tester('(if (>= 0 1) "Zero is less than one" "Zero is not less than one")',
           '"Zero is not less than one"')
    tester('(if (= 0 (+ 5 -3 -2)) "True" "False")', '"True"')
    tester('(if (not (= 0 (+ 5 -3 -2))) "True" "False")', '"False"')


def test_set_f():
    tester('(set! a 2) (+ a 5)', [None, 7])
    tester('(set! a aaaa) (string-append a bbbb)', [None, "aaaa bbbb"])


def test_begin():
    tester('(begin (display 2) (display 5))', None)


def test_define_f():
    tester('(define a 2) (+ a 5)', [None, 7])
    tester('(define a aaaa) (string-append a bbbb)', [None, "aaaa bbbb"])
    tester('(define (sq x) (* x x)) (sq 9) (sq 15)', [None, 81, 225])
    tester('(define (averagenum n1 n2 n3 n4) (/ ( + n1 n2 n3 n4) 4)) \
    (averagenum 10 20 30 40) (averagenum 5 10 15 20)', [None, 25, 12.5])
    tester('(define (gcd a b) (if (= b 0) a (gcd b (remainder a b))))\
    (gcd 8 12)(gcd 498 444)', [None, 4, 6])
    tester('(define (factorial x) (if (= x 0) 1 (* x (factorial (- x 1)))))\
    (factorial 6)', [None, 720])


def test_lambda_f():
    tester('((lambda (a b) (+ (* 2 a) b)) 5 6)', 16)
    tester('((lambda (x) (* x x)) 8)', 64)


def test_list_f():
    tester('(list 1 2 3)', [1, 2, 3])
    tester('(list 1 2 "aaa")', [1, 2, '"aaa"'])


def test_car_f():
    tester('(car 1 2 3)', 1)
    tester('(car "aaa" 4 5)', '"aaa"')


def test_cdr_f():
    tester('(cdr 1 2 3)', [2, 3])
    tester('(cdr "aaa" 4 5)', [4, 5])


def test_cons_f():
    tester('(cons (list 1 2 3) (list 4 5))', [1, 2, 3, 4, 5])
    tester('(cons (list "aaa" 2 3) (list 4 5))', ['"aaa"', 2, 3, 4, 5])


def test_append_f():
    tester('(append (list 1 2 3) (list 4 5))', [1, 2, 3, 4, 5])
    tester('(append (list "aaa" 2 3) (list 4 5))', ['"aaa"', 2, 3, 4, 5])


def main():
    test_append_f()
    test_cons_f()
    test_cdr_f()
    test_car_f()
    test_list_f()
    test_lambda_f()
    test_define_f()
    test_begin()
    test_set_f()
    test_if_f()
    test_newline()
    test_display()
    test_string_append_f()
    test_remainder_f()
    test_round_f()
    test_null_ch()
    test_number_ch()
    test_symbol_ch()
    test_list_ch()
    test_not_f()
    test_or_f()
    test_and_f()
    test_min_f()
    test_max_f()
    test_op_abs()
    test_equal_ch()
    test_eq_ref_ch()
    test_op_eq()
    test_op_le()
    test_op_ge()
    test_op_lt()
    test_op_gt()
    test_op_truediv()
    test_op_mul()
    test_op_sub()
    test_op_add()


if __name__ == "__main__":
    main()
