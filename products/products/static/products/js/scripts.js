const newReviewForm = $("#newUserReview > form")
const reviewContent = $("#id_review_content")
const reviewSubmit = $("#reviewSubmitButton")
const editReview = $("#editReview")
const categories = ["implant", "app", "upgrade"]
const productFilterButton = $(".product-filter-button")
const filterActive = "js-product-filter-button__active"

/* Enables form to add or edit review.*/
const enableReviewForm = () => {
	reviewContent.removeAttr("disabled")
	reviewSubmit.parent().addClass("d-block")
	newReviewForm.addClass("d-block")
	editReview
		.attr("id", "cancelEditReview")
		.removeClass("far fa-edit")
		.addClass("fas fa-times")
}

/*Disables form to add or edit review.*/
const disableReviewForm = () => {
	reviewContent.attr("disabled", "true")
	reviewSubmit.parent().removeClass("d-block")
	newReviewForm.removeClass("d-block")
	$("#cancelEditReview")
		.attr("id", "editReview")
		.removeClass("fas fa-times")
		.addClass("far fa-edit")
}

/*Gets id to be filtered.
 @returns {string} id of element*/
const getFilterId = () => {
	return _this.attr("id")
}

/*Clears filter to display all products.*/
const clearFilter = () => {
	categories.forEach((cat) => {
		$(`.js-filter-${cat}`).removeClass("d-none")
		$(`#${cat}`).removeClass(filterActive)
	})
}

/*Filters by matching id
 * @param {string} id the id of the elements to be filtered*/
const filterById = (id) => {
	categories.forEach((cat) => {
		if (cat == id) {
			$(`.js-filter-${cat}`).removeClass("d-none")
			$(`#${cat}`).addClass(filterActive)
		} else {
			$(`.js-filter-${cat}`).addClass("d-none")
			$(`#${cat}`).removeClass(filterActive)
		}
	})
}

// Adds a click event to all matching buttons
document.querySelectorAll(".product-filter-button").forEach((element) => {
	element.addEventListener("click", function (e) {
		e.preventDefault()
		_this = $(this)
		if (this.classList.contains("js-product-filter-button__active")) {
			clearFilter()
		} else {
			productFilterButton.removeClass("js-product-filter-button__active")
			this.classList.add("js-product-filter-button__active")
			filterId = getFilterId()
			filterById(filterId)
		}
	})
})

$(document).ready(function () {
	$(document).on("click", "#editReview", function () {
		enableReviewForm()
	})
	$(document).on("click", "#cancelEditReview", function () {
		disableReviewForm()
	})
})
