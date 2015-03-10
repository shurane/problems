#lang racket

; haskell naming
(define (init lst)
  (match lst
    ['()  (error "empty list")]
    [_    (take lst (- (length lst) 1))]))

(define (palindromify-chars s)
  (cond
    [(eq? (length s) 0) 0]
    [(eq? (length s) 1) 0]
    [(eq? (length s) 2) (abs (- (char->integer (first s)) 
                                (char->integer (last s))))]
    [else
      (+
         (abs (- (char->integer (first s))
              (char->integer (last s))))
         (palindromify-chars (rest (init s))))]))

(define (palindromify s)
  (palindromify-chars (string->list s)))

(define (readlines n)
  (if (eq? n 0)
    (list)
    (cons (read-line)
          (readlines (- n 1)))))

(define T (string->number (read-line)))
(define args (readlines T))

(for ([arg args])
  (printf "~a~n" (palindromify arg)))
