#lang racket

(define (keep-reading)
  (define line (read-line))
  (if (eof-object? line)
    (list)
    (cons line (keep-reading))))

(define (replace-line-comments s)
  (regexp-replace* #rx"//.*?\n" s "\n"))
(define (replace-block-comments s)
  (regexp-replace* #rx"/\\*.*?\\*/" s ""))

; use positive-lookahead
(define (match-line-comments s)
  (regexp-match* #rx"//.*?(?=\n)" s))
(define (match-block-comments s)
  (regexp-match* #rx"/\\*.*?\\*/" s))
(define (match-both-comments s)
  (regexp-match* #rx"//.*?(?=\n)|/\\*.*?\\*/" s))

(define (strip-leading-whitespace s)
;|^[[:space:]]* <-- not needed I think
  (regexp-replace* #px"\n[[:space:]]*" s "\n"))

(define input (string-join (keep-reading) "\n"))
(for ([comment (match-both-comments input)])
  (displayln (strip-leading-whitespace comment)))
