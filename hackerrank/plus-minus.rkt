#lang racket

(define N (string->number (read-line)))
(struct Statistic (positive negative zero) #:transparent)
(define nums (map string->number (string-split (read-line))))

;(foldl
  ;(lambda (num stat)
    ;(displayln stat)
    ;(struct-copy Statistic stat [positive (+ (Statistic-positive stat) 1)]))
  ;(Statistic 0 0 0)
  ;nums)

(define nums-stat
  (foldl 
    (lambda (num stat)
      (cond
        [(positive? num) 
         (struct-copy Statistic stat [positive (+ (Statistic-positive stat) 1)])]
        [(negative? num) 
         (struct-copy Statistic stat [negative (+ (Statistic-negative stat) 1)])]
        [(zero? num) 
         (struct-copy Statistic stat [zero (+ (Statistic-zero stat) 1)])]
        ))
    (Statistic 0 0 0)
    nums))

(displayln (~r (exact->inexact (/ (Statistic-positive nums-stat) N)) #:precision '(= 6)))
(displayln (~r (exact->inexact (/ (Statistic-negative nums-stat) N)) #:precision '(= 6)))
(displayln (~r (exact->inexact (/ (Statistic-zero nums-stat) N)) #:precision '(= 6)))

