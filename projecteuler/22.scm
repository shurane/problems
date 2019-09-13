#lang racket

(define (score name)
  (foldl + 0
    (for/list ([c name])
      (+ (- (char->integer c) (char->integer #\A)) 1))))

(define names-unclean (regexp-split #px"," (file->string "22-names.txt")))
(define names 
  (sort 
    (for/list ([i names-unclean]) (string-replace i "\"" ""))
    string<?))
(define names-with-index 
  (map list (range 1 (+ (length names) 1)) names))

(foldl (lambda (l result) (+ (* (first l) (score (second l))) result))
         0 
         names-with-index)
;(length names-with-index)
