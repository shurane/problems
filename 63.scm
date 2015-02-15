#lang racket

(require racket/pretty)

(define ztow
 (for*/list
   ([i (in-range 1 100)]
    [j (in-range 1 100)])
   (list i j (expt i j))))

(define n-digit-powers
  (filter
    (lambda (l)
      (eq?
        (cadr l)
        (string-length (number->string (caddr l)))))
  ztow))

(pretty-print n-digit-powers)
(pretty-print (length n-digit-powers))
