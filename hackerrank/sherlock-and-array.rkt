#lang racket

; https://www.hackerrank.com/challenges/sherlock-and-array
; TODO this is slow on big inputs, check input files

(define (solve-case c)
  (let* ([n (first c)]
         [array (second c)]
         [left 0]
         [right (sequence-fold + 0 array)]
         [elems (for/vector ([i (in-range n)])
           ;(format "solve-case left:~a middle:~a right:~a ~n" 
           ;(list
             ;(vector-take array i) 
             ;(vector-ref array i)
             ;(vector-drop array (+ i 1))))]
           (set! left (+ left (sequence-ref array i)))
           (set! right (- right (sequence-ref array i)))
           (list
             left
             (sequence-ref array i)
             right))]
         [results (vector-filter equal-left-right elems)])
         (if (= (sequence-length results) 0)
           "NO"
           "YES")))

(define (equal-left-right elems)
  (= (sequence-fold + 0 (first elems)) 
     (sequence-fold + 0 (third elems))))

; TODO this is better done as a struct? or something instead of just a list
(define (grab-case)
  (let ([n      (string->number (read-line))]
        [array  (list->vector (map string->number (string-split (read-line))))])
    (list n array)))

(define (grab-all-cases t)
  (if (eq? t 0)
    (list)
    (cons (grab-case) (grab-all-cases (- t 1)))))

(define T (string->number (read-line)))
(define cases (grab-all-cases T))

(for ([c cases])
  (displayln (solve-case c)))
