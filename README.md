# Roman Numerals Coding Dojo

## Organizational Rules
* One person is the driver; (s)he will actually decide what code to write.
* One person is the navigator; (s)he will assist the driver by keeping an eye on the current objective of the test and by spotting errors/typos.
* The rest are spectators; usually they should not interfere as not to disturb the driver, navigator pair
* Every 5/7/10 minutes we will rotate: navigator will become driver, driver will join the spectators and one spectator will become the new navigator
* This will happen round robin; this dojo style is called a 'Randori'

## Red/Green TDD Approach (Coding Rules)
* Write a Test that is failing against an unimplemented or partially implemented function
* Ensure the test is Red (if not, investigate if that is by accident, or if the full desired behaviour the test should ensure is covered)
* Commit the result
* Implement the functionality to make the test Green (and nothing else!)
* Commit the result
* Refactor as necessary while keeping the test green.
* Commit the result

## When the Clock runs out
* Two choices: either we can directly push, or there is stuff that could potentially be committed
* BUT: usually only failing *new* tests or *green* tests are committed.
* It might happen that a driver has coded him/herself into a corner.
* Next driver (current navigator) gets to decide wether to revert or commit before the push
* Push all that has been committed.
* Next Driver pulls and continues. Of course screen sharing needs to be switched accordingly.
