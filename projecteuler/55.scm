#lang racket

; see http://jeapostrophe.github.io/2013-08-19-reverse-post.html
(define (reverse-number number)
  (string->number (list->string (reverse (string->list (number->string number))))))

(define (is-lychrel n [upto 50])
  (let loop ([number n]
             [r-number (reverse-number n)]
             [count 0])
    (let ([result (+ number r-number)])
      ;(printf "number:~a r-number:~a result:~a count:~a ~n" number r-number result count)
      (cond
        [(eq? (reverse-number result) result) #f]
        [(>= count upto) #t]
        [else
          (loop result (reverse-number result) (+ count 1))]))))

(length (filter (lambda (l)  (eq? #t (cadr l)))
  (for/list ([number (range 1 1e4)])
    (list number (is-lychrel number)))))

