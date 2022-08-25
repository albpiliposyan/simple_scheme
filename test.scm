(list 1 2 3)
(newline) (display "SQUARE") (newline)
(define (sq x) (* x x))
(display (sq 9))
(newline)
(display (sq 15))
(newline)


(newline) (display "AVERAGE NUMBER") (newline)
(define (average n1 n2 n3 n4) (/ ( + n1 n2 n3 n4) 4))
(display (average 10 20 30 40))
(newline)
(display (average 1 8 9 5))
(newline)


(newline) (display "GCD") (newline)
(define (gcd a b) (if (= b 0) a (gcd b (remainder a b))))
(display (gcd 8 12))
(display (gcd 498 444))
(newline)


(newline) (display "FACTORIAL OF 6") (newline)
(define (factorial x) (if (= x 0) 1 (* x (factorial (- x 1)))))
(display (factorial 6))
(newline)


(newline) (display "LAMBDA") (newline)
(display ((lambda (a b) (+ (* 2 a) b)) 5 6))
(newline)


;(newline)
;(display "CHECKING AN ERROR MESSAGE")
;(+ "test" 15)
;(newline)


(newline) (display "ROUND") (newline)
(display (round (+ 8 0.55)))
(newline)


(newline) (display "LIST") (newline)
(list 1 2 3)
(display (list 4 9 (+ 9 5))) (newline)
(display (list? (list 1 2 3)))
(newline)


(newline) (display "OR") (newline)
(display (or (> 8 655) (> 1 45)))
(newline)


(newline) (display "IF-ELSE STATEMENT") (newline)
(if (< 1 8) (display "1 is less than 8") (display "FALSEEE"))
(newline)


(newline) (display "MATHEMATICAL EXPRESSION") (newline)
(display (+ 2 2 2 (- 10 5) 2 2 (/ 100 ( * 2 5))))
(newline)


(newline) (display "BEGIN") (newline)
(begin (display "A") (display (- 10 10)) (display "B"))
(newline)


(newline) (display "SET! - DEFINE") (newline)
(set! a 40)
(define k 10)
(define k 50)
(define c "test variable3")
(display (- (+ a k) 10 (* 2 2 5)))
(+ 78 9 (- 4 9 ) 87 (* 7 9))
(newline)
