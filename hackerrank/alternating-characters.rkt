#lang racket

; not the greatest, code seems a little inconsistent.
; it should be made to generalize though.

(define (alternating? s)
  (let ([sl (string-length s)])
    (cond
      [(<= sl 1) #t]
      [(or (eq? s "AB")
           (eq? s "BA")) #t]
      [(or (eq? s "AA")
           (eq? s "BB")) #f]
      [ else (and
               (not (eq? (string-ref s 0)
                         (string-ref s 1)))
               (alternating? (substring s 1)))])))

; the other way is to look for A+ and reduce to A
;                              B+ and reduce to B
(define (make-alternating-2 s)
  (cond
   [(alternating? s) s]
   [(eq? (string-ref s 0) (string-ref s 1))
    (string-append (substring s 0 1)
                   ; kind of messy set of chained calls
                   (make-alternating-2
                     (list->string
                       (dropf
                         (string->list (substring s 2))
                         ((curry eq?) (string-ref s 0))))))]
   [else
     (string-append (substring s 0 1)
                   (make-alternating-2 (substring s 1)))]))

(define (make-alternating s)
  (regexp-replaces s
    '(
      [#rx"A+" "A"]
      [#rx"B+" "B"])))


(define (make-alternating-diff s)
  (let ([alternated (make-alternating s)])
    (list alternated (- (string-length s)
                        (string-length alternated)))))

(define (readlines n)
  (if (eq? n 0)
    (list)
    (cons (read-line)
          (readlines (- n 1)))))

(define T (string->number (read-line)))
(define args (readlines T))

(for ([arg args])
  (printf "~a~n" (cadr (make-alternating-diff arg))))
