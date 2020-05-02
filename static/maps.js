(function($) {
    DjangoGooglePointFieldWidget = DjangoMapWidgetBase.extend({

        initializeMap: function(){
            var mapCenter = this.mapCenterLocation;
            if (this.mapCenterLocationName){
                
                this.geocoder.geocode({'address' : this.mapCenterLocationName}, function(results, status) {
                    if (status === google.maps.GeocoderStatus.OK) {
                        var geo_location = results[0].geometry.location;
                        mapCenter = [geo_location.lat(), geo_location.lng()];
                    }else{
                        console.warn("Cannot find " + this.mapCenterLocationName + " on google geo service.")
                    }
                    this.map = new google.maps.Map(this.mapElement, {
                        center: new google.maps.LatLng(mapCenter[0], mapCenter[1]),
                        scrollwheel: false,
                        zoomControlOptions: {
                            position: google.maps.ControlPosition.RIGHT
                        },
                        zoom: this.zoom
                    });

                    $(this.mapElement).data('google_map', this.map);
                    $(this.mapElement).data('google_map_widget', this);

                    if (!$.isEmptyObject(this.locationFieldValue)){
                        this.updateLocationInput(this.locationFieldValue.lat, this.locationFieldValue.lng);
                        this.fitBoundMarker();
                    }

                }.bind(this));

            }else{
                this.map = new google.maps.Map(this.mapElement, {
                    center: new google.maps.LatLng(mapCenter[0], mapCenter[1]),
                    scrollwheel: false,
                    zoomControlOptions: {
                        position: google.maps.ControlPosition.RIGHT
                    },
                    zoom: this.zoom
                });
                
                $(this.mapElement).data('google_map', this.map);
                $(this.mapElement).data('google_map_widget', this);

                if (!$.isEmptyObject(this.locationFieldValue)){
                    this.updateLocationInput(this.locationFieldValue.lat, this.locationFieldValue.lng);
                    this.fitBoundMarker();
                }
            }

        },

        addMarkerToMap: function(lat, lng){
            this.removeMarker();
            var marker_position = {lat: parseFloat(lat), lng: parseFloat(lng)};
            this.marker = new google.maps.Marker({
                position: marker_position,
                map: this.map,
                draggable: true
            });
            this.marker.addListener("dragend", this.dragMarker.bind(this));
        },

        fitBoundMarker: function () {
            var bounds = new google.maps.LatLngBounds();
            bounds.extend(this.marker.getPosition());
            this.map.fitBounds(bounds);
            if (this.markerFitZoom && this.isInt(this.markerFitZoom)){
                var markerFitZoom = parseInt(this.markerFitZoom);
                var listener = google.maps.event.addListener(this.map, "idle", function() {
                    if (this.getZoom() > markerFitZoom) {
                        this.setZoom(markerFitZoom)
                    }
                    google.maps.event.removeListener(listener);
                });
            }
        },

        removeMarker: function(e){
            if (this.marker){
                this.marker.setMap(null);
            }
        },

        dragMarker: function(e){
            this.updateLocationInput(e.latLng.lat(), e.latLng.lng())
        },

        handleAddMarkerBtnClick: function(e){
            $(this.mapElement).toggleClass("click");
            this.addMarkerBtn.toggleClass("active");
            if ($(this.addMarkerBtn).hasClass("active")){
                this.map.addListener("click", this.handleMapClick.bind(this));
            }else{
                google.maps.event.clearListeners(this.map, 'click');
            }
        },

        handleMapClick: function(e){
            google.maps.event.clearListeners(this.map, 'click');
            $(this.mapElement).removeClass("click");
            this.addMarkerBtn.removeClass("active");
            this.updateLocationInput(e.latLng.lat(), e.latLng.lng())
        }
    });

})(mapWidgets.jQuery);


var mapWidgets = mapWidgets || {};

// Use Django Admin jQuery function if exists, otherwise initialise `mapWidgets.jQuery` from global jQuery.
if (typeof django !== "undefined" && django.jQuery){
    mapWidgets.jQuery = django.jQuery.noConflict();
}else{
    mapWidgets.jQuery = jQuery.noConflict();
}


var mapWidgets = mapWidgets || {};
if (typeof django !== "undefined" && django.jQuery){
    mapWidgets.jQuery = django.jQuery.noConflict();
}else{
    mapWidgets.jQuery = jQuery.noConflict();
}


(function($) {

    var initializing = false, fnTest = /xyz/.test(function(){xyz;}) ? /\bSuper\b/ : /.*/;

    $.Class = function() {

    };

    $.Class.extend = function(prop) {
        var Super = this.prototype;

        initializing = true;
        var prototype = new this();
        initializing = false;

        for (var name in prop) {
            prototype[name] = typeof prop[name] == "function" && typeof Super[name] == "function" && fnTest.test(prop[name]) ? (function(name, fn) {
                return function() {
                    var tmp = this.Super;

                    this.Super = Super[name];

                    var ret = fn.apply(this, arguments);
                    this.Super = tmp;

                    return ret;
                };
            })(name, prop[name]) : prop[name];
        }

        function Class() {
            if (!initializing && this.init) {
                this.init.apply(this, arguments);
            }
        }

        Class.prototype = prototype;

        Class.constructor = Class;

        Class.extend = arguments.callee;

        return Class;
    };

    if (typeof Function.bind === 'undefined') {

        Function.prototype.bind = function(obj) {
            var method = this;

            tmp = function() {
                return method.apply(obj, arguments);
            };

            return tmp;
        };

    }

    if (!Array.indexOf){
        Array.prototype.indexOf = function(obj) {
            for (var i = 0; i < this.length; i++) {
                if (this[i] == obj) {
                    return i;
                }
            }

            return -1;
        };
    }

})(mapWidgets.jQuery);