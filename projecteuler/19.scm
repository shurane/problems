#lang racket

(define years (range 1901 (+ 2000 1)))
(define months (range 1 (+ 12 1)))
(define weekday (range 1 (+ 7 1)))
(define (leap-year? year)
  (if (and
        (eq? (modulo year 4) 0)
        (not (and 
               (eq? (modulo year 100) 0)
               (not (eq? (modulo year 400) 0)))))
    #t
    #f))

(define (days-in-month year month)
  (cond
    [(eq? month 1 ) 31]
    [(eq? month 2 ) (if (leap-year? year) 29 28)]
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

(define ym (for*/list 
             ([year years]
              [month months])
    (list year month (days-in-month year month))))

(define ym-accum 
  (reverse (foldl (lambda (i result) (cons 
                            (+ (car result) (caddr i)) 
                            result))
       (list 0) ym)))

(length (filter (lambda (i) (eq? (modulo i 7) 0)) ym-accum))
