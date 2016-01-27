#lang racket

(define time-string (read-line))
(define time-left (substring time-string 0 8))
(define meridian (substring time-string 8))
(define-values (hours minutes seconds) 
               (apply values
                 (map string->number (string-split time-left ":"))))

; it's alright, because the two set! conditions don't overlap

(set! hours
  (if
    (and 
      (equal? meridian "PM")
      (not (equal? hours 12)))
    (+ hours 12)
    hours))

(set! hours
  (if
    (and
      (equal? meridian "AM")
      (equal? hours 12))
    0
    hours))

(displayln (string-append
             (~r hours #:min-width 2 #:pad-string "0") 
             ":"
             (~r minutes #:min-width 2 #:pad-string "0") 
             ":"
             (~r seconds #:min-width 2 #:pad-string "0")))
