;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname |ticket profits|) (read-case-sensitive #t) (teachpacks ((lib "image.rkt" "teachpack" "htdp"))) (htdp-settings #(#t constructor repeating-decimal #f #t none #f ((lib "image.rkt" "teachpack" "htdp")) #f)))
;price 5 per ticket 120 atendees
;average attendence chenged by 15 people if price changes 5.10, 105 people attend
;if price goes to 4.90 attendence increases to 135
; idea into math (Av.Attendence = (120 people less ($(change in price)/0.10)*15 people)

(define (attendees ticket-price)
  (- 120 (* (- ticket-price 5.0) (/ 15 0.1))))

(define (revenue ticket-price)
  (* ticket-price (attendees ticket-price)))

(define (cost ticket-price)
  (+ 180 (* 0.4 (attendees ticket-price))))
;there are fixed costs of 180 and variable that depend on number of attendees
;the variable costs are a percentage

(define (profit ticket-price)
  (- (revenue ticket-price)
     (cost ticket-price)))