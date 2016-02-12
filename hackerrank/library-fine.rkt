#lang racket

(struct Date (d m y) #:transparent)

(define actual-date (apply Date (map string->number (string-split (read-line)))))
(define expected-date (apply Date (map string->number (string-split (read-line)))))
; not the best way... but it works
(define difference (Date 
                    (- (Date-d actual-date) (Date-d expected-date))
                    (- (Date-m actual-date) (Date-m expected-date))
                    (- (Date-y actual-date) (Date-y expected-date))))

; man, so imperative, might as well introduce set!
(define (fine date)
  (cond 
    [(and 
       (= (Date-y date) 0)
       (= (Date-m date) 0)
       (> (Date-d date) 0))
     (* 15 (Date-d date))]
    [(and 
       (= (Date-y date) 0)
       (> (Date-m date) 0))
     (* 500 (Date-m date))]
    [(and 
       (> (Date-y date) 0))
     10000]
    [else 
      0]))

;(displayln actual-date)
;(displayln expected-date)
(displayln (fine difference))
