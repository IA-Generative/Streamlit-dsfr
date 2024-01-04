<script setup lang="ts">
import { ref, onMounted, onUpdated, onUnmounted, onErrorCaptured } from 'vue'
import { Streamlit, type RenderData } from '~/stcomponentlib'

const renderData = ref<RenderData | undefined>(undefined)
const componentError = ref<string | undefined>(undefined)
const innerWidth = ref<number>(NaN)

const onRenderEvent = (event: Event): void =>
	{
		const renderEvent = event as CustomEvent<RenderData>
		renderData.value = renderEvent.detail
		componentError.value = undefined
		innerWidth.value = window.innerWidth
	}

onMounted(() =>
	{
		Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
		Streamlit.setComponentReady()
	})

onUpdated(() =>
	{
		if (componentError.value !== undefined)
		{
			Streamlit.setFrameHeight()
		}
	})

onUnmounted(() =>
	{
		Streamlit.events.removeEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
	})

onErrorCaptured(err =>
	{
		componentError.value = String(err)
	})
</script>

<template>
	<div>
		<div v-if="componentError !== undefined">
			<h1 class="err__title">Component Error</h1>
			<div class="err__msg">Message: {{ componentError }}</div>
		</div>
		<slot
			v-else-if="renderData !== undefined"
			:width="innerWidth"
			:args="renderData.args"
			:disabled="renderData.disabled"
			:theme="renderData.theme"
		></slot>
	</div>
</template>

<style scoped>
.err__title,
.err__msg {
  	margin: 0;
}
</style>
