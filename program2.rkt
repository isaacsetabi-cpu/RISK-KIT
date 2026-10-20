;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname program2) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "htdp")) #f)))
(define x 3)
(define y 4)
(define prefix "hello")
(define suffix "world")
(define sunny #true)
(define friday #false)

(define (distance x y)
    (cond
      ([<= y 0] x) ;base case when movement is on a single plane
      ([>= y 0]
       (sqrt (+ (expt x 2) (expt y 2)))))) ; computing the distance with the root
                                           ;of the square distances

(define (addtwo prefix suffix)
  (cond
    ([>= (string-length suffix) 0]
     (string-append prefix "_" suffix))
     ))

(define (shoping day temp)
  (or (< temp 25) (= day Friday))
    )
     