;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname functionsmore) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "htdp")) #f)))
;NUMBER -> NUMBER
;COMPUTES THE AREA OF A SQUARE WITH SIDE LEN
;GIVEN: 2 EXPECT: 4
;GIVEN: 6 EXPECT: 36
(define (area-of-square len)
  (sqr len))

;NUMBER STRING IMAGE -> IMAGE
;ADD S TO IMAGE, Y PIXELS FROM THE TOP, 10 PIXELS TO THE LEFT
;GIVEN
;  5 FOR Y 
;  "HELLOW" FOR S AND
;   (EMPTY-SCENE 100 100) FOR IMG
;EXPECTED:
;    (PLACE-IMAGE (TEXT "HELLOW" 10 "RED") 10 5 ...)
;    (WHERE .... IS (EMPTY-SCENE 100 100)
(define (add-image y s img)
  (place-image (text s 10 "red") 10 y img))

;STRING->STRING
;GIVEN:
;    "HELLOW" FOR S
;EXPECTED:
;    "H"
(define (string-first s)
  (substring s 0 1))

(define (string-remove-last s)
  (substring s 0 (- (string-length s) 1)))

(define (string-last s)
  (substring s (- (string-length s) 1)
             (string-length s) ))

(define (string-rest s)
  (substring s 1 (string-length s)))

;NUMBER -> NUMBER
;Converts Fahrenheit to celsius
;given 32, expect 0
;given 212, expect 100
(define (f2c f)
  (* 5/9 (- f 32)))