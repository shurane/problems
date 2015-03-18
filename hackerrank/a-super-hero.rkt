#lang racket

(require racket/pretty)

(define (readlines n)
  (if (eq? n 0)
    (list)
    (cons (map string->number
           (regexp-split 
             #px" " 
             (read-line)))
          (readlines (- n 1)))))

(define (read-game)
  (let* ([nm (map string->number 
               (regexp-split 
                 #px" " 
                 (read-line)))]
         [n (first nm)]
         [m (second nm)]
         [levels-with-power (readlines n)]
         [levels-with-bullets (readlines n)])
    (list levels-with-power levels-with-bullets)))

(define T (string->number (read-line)))

(define (readgames t)
  (if (eq? t 0)
    (list)
    (cons (read-game) (readgames (- t 1)))))

(pretty-print (readgames T))
