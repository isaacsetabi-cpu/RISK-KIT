;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname ticket2) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "htdp")) #f)))
(define PRICE-VOLTILITY (/ 15 0.1))

(define (attendees ticket-price)
  (- 120 (* (- ticket-price 5.0) PRICE-VOLTILITY)))

(define (revenue ticket-price)
  (* ticket-price (attendees ticket-price)))

(define (cost ticket-price)
  (+ 180 (* 0.4 (attendees ticket-price))))

(define (profit ticket-price)
  (- (revenue ticket-price)
     (cost ticket-price)))

; on top of the functions defined in the program, there are two more programs
; 1. the batch program it consumes all inputs at once and computes its results.
; 2. its main function is to compose suport functions
; 3. the interactive program, this consumes some of its inputs, computes,
; produces an output consumes more input and the cycle repeats
; when an input appears, we call an event
; the functions are:
; read-file; it reads the content of the entire file as a string
; write-file; it creates a file from a given string