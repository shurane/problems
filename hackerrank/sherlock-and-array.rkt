#lang racket

; https://www.hackerrank.com/challenges/sherlock-and-array

(define (solve-case c)
  (let* ([c-length (first c)]
         [c-elems (second c)]
         [elems (for/list ([i (in-range c-length)])
           ;(format "solve-case left:~a middle:~a right:~a ~n" 
           (list
             (take c-elems i) 
             (list-ref c-elems i)
             (drop c-elems (+ i 1))))]
         [results (filter equal-left-right elems)])
         (if (= (length results) 0)
           "NO"
           "YES")))

(define (equal-left-right elems)
  (= (apply + (first elems)) 
     (apply + (third elems))))

(define (grab-case)
  (let ([n      (string->number (read-line))]
        [array  (map string->number (string-split (read-line)))])
    (list n array)))

(define (grab-all-cases t)
  (if (eq? t 0)
    (list)
    (cons (grab-case) (grab-all-cases (- t 1)))))

(define T (string->number (read-line)))
(define cases (grab-all-cases T))

(for ([c cases])
  (displayln (solve-case c)))
