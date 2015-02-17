#lang racket

(define years (range 1901 2000))
(define months (range 1 12))
(define (leap-year year)
  (if (and
        (eq? (modulo year 4) 0)
        (not (and 
               (eq? (modulo year 100) 0)
               (not (eq? (modulo year 400) 0)))))
    #t
    #f))

(define (day-of-week year month day)
  'something)

(define (days-in-months year month)
  (cond
    [(eq? month 1 ) 31]
    [(eq? month 2 ) (if (leap-year year) 29 28)]
    [(eq? month 3 ) 31]
    [(eq? month 4 ) 30]
    [(eq? month 5 ) 31]
    [(eq? month 6 ) 30]
    [(eq? month 7 ) 31]
    [(eq? month 8 ) 31]
    [(eq? month 9 ) 30]
    [(eq? month 10) 31]
    [(eq? month 11) 30]
    [(eq? month 12) 31]
    [else (error "shouldn't get here")]))

