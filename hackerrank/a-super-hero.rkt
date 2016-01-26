#lang racket

; TODO not working

; haskell naming
(define (init lst)
  (match lst
    ['()  (error "empty list")]
    [_    (take lst (- (length lst) 1))]))

(define (sliding-window lst [size 2] [skip 1])
  (if (< (length lst) size)
    empty-stream
    (stream-cons 
      (take lst size)
      (sliding-window (drop lst skip) size skip))))

(define (2d-print lstoflst)
  (string-join
    (for/list ([row lstoflst])
      (format "~a~n" row))
    ""))

(define (2d-list-ref lstoflst x y)
  (list-ref (list-ref lstoflst y) x))

(define (readlines n)
  (if (eq? n 0)
    (list)
    (cons (map string->number
           (regexp-split
             #px" "
             (read-line)))
          (readlines (- n 1)))))

(define (solve-game game)
  ; UHOH the read-game method does all the solving...
  'TODO)

(define (read-game)
  (let* ([nm (map string->number
               (regexp-split
                 #px" "
                 (read-line)))]
         [n (first nm)]
         [m (second nm)]
         [levels-with-power (readlines n)]
         [levels-with-bullets (readlines n)]
         [levels-with-power-minus-bullets
           (map (curry map -)
                      levels-with-power
                      levels-with-bullets)]
         [levels-with-max-bullets-from-prev-level
           (cons 
             (first levels-with-power-minus-bullets)
             (for/list ([pair (sliding-window levels-with-power-minus-bullets)])
               (let ([max-bullets-from-prev-level (apply max (first pair))])
                 (map 
                   (lambda (x) (- x max-bullets-from-prev-level))
                   ;(curry + max-bullets-from-prev-level) 
                   (second pair)))))]
         [levels-min
           (map (curry apply min)
                  levels-with-max-bullets-from-prev-level)]
         [bullets-needed
           (apply +
             (filter positive? levels-min))])
    (printf "levels-with-power:~n~a"
      (2d-print levels-with-power))
    (printf "levels-with-bullets:~n~a"
      (2d-print levels-with-bullets))
    (printf "levels-with-power-minus-bullets:~n~a"
      (2d-print levels-with-power-minus-bullets))
    (printf "levels-with-max-bullets-from-prev-level:~n~a"
      (2d-print levels-with-max-bullets-from-prev-level))
    (printf "levels-min:~n~a~n" 
      levels-min)
    (+ bullets-needed 1))) ; include initial bullet

(define T (string->number (read-line)))

(define (readgames t)
  (if (eq? t 0)
    (list)
    (cons (read-game) (readgames (- t 1)))))

(for ([bullets-needed (readgames T)])
  (displayln bullets-needed))
