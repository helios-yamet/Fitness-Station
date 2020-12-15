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