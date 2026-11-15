# README

## Why is LibraryItem abstract, and what happens if DVD forgets to write late_fee()?
`LibraryItem` is abstract because it serves as a blueprint for all library items, ensuring that every subclass implements the `late_fee()` method. If `DVD` forgets to implement `late_fee()`, Python will raise a `TypeError` when trying to instantiate `DVD`, as it would not fulfill the abstract method requirement.

## What happens when you read item.__available from outside the class, and why do we use is_available() instead?
Attempting to access `item.__available` from outside the class raises an `AttributeError` because `__available` is a private attribute. The `is_available()` method is provided as a public interface to safely check the availability status without directly exposing the private attribute.

## What is the difference between LibraryItem.total_items and self.title?
`LibraryItem.total_items` is a class attribute shared across all instances, tracking the total number of library items created. In contrast, `self.title` is an instance attribute specific to each object, representing the title of that particular library item.