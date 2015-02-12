#lang racket

(define number-letter-mapping (make-hash (list
      '(1 "one")
      '(2 "two")
      '(3 "three")
      '(4 "four")
      '(5 "five")
      '(6 "six")
      '(7 "seven")
      '(8 "eight")
      '(9 "nine")
      '(10 "ten")
      '(11 "eleven")
      '(12 "twelve")
      '(13 "thirteen")
      '(14 "fourteen")
      '(15 "fifteen")
      '(16 "sixteen")
      '(17 "seventeen")
      '(18 "eighteen")
      '(19 "nineteen")
      '(20 "twenty")
      '(30 "thirty")
      '(40 "fourty")
      '(50 "fifty")
      '(60 "sixty")
      '(70 "seventy")
      '(80 "eighty")
      '(90 "ninety")
      ; TODO more clever way to generate for hundreds, thousands, etc?
      '(100 "one hundred")
      '(200 "two hundred")
      '(300 "three hundred")
      '(400 "four hundred")
      '(500 "five hundred")
      '(600 "six hundred")
      '(700 "seven hundred")
      '(800 "eight hundred")
      '(900 "nine hundred")
      '(1000 "one thousand"))))

; haskell naming
(define (init lst)
  (match lst
    ['()  (error "empty list")]
    [_    (take lst (- (length lst) 1))]))

; Martin Neal says it's better to do an inner-define
; http://stackoverflow.com/a/7133473/198348
(define (digitize-backwards n)
  (define (digitize-backwards n place-value)
    (let ([digit-place (* (modulo n 10) place-value)])
      (if (< n 10)
        (list digit-place)
        (cons digit-place
              (digitize-backwards
                (floor (/ n 10))
                (* place-value 10))))))
  (digitize-backwards n 1))

(define (digitize n)
   (reverse (digitize-backwards n)))

(define (number->letter n)
  (let* ([digits (digitize n)]
         [digit-pairs (reverse (map
                                list
                                (init digits)
                                (cdr digits)))])
    (reverse digits)))

; TODO go from back of list to front with a left and right iterator of sorts
; Soooo '(1000 700 40 3) --> (list '(40 3) '(700 40) '(1000 700))
(printf "got: ~a~n" (number->letter 18))
;(printf "~a~n" (number->letter 21))
;(printf "~a~n" (number->letter 118))
;(printf "~a~n" (number->letter 121))
(printf "got: ~a~n" (number->letter 123))
(printf "got: ~a~n" (number->letter 1373))
