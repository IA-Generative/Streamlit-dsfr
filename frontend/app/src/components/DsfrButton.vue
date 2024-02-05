<script setup lang="ts">
import { onMounted, onUnmounted, ref, computed } from 'vue'
import { Streamlit } from '~/stcomponentlib'

import '~/assets/iconify-icon.min.js'

import { useStreamlit } from '~/streamlit'
import type { ComponentProps } from '~/types/ComponentProps.d.ts'
import DsfrButton from '~/components/dsfr/DsfrButton.vue'

useStreamlit()

const props = defineProps<
	ComponentProps<{
		label?: string
		secondary?: boolean
		tertiary?: boolean
		disabled?: boolean
		icon?: string
		iconOnly?: boolean
		iconRight?: boolean
		noOutline?: boolean
		size?: '' | 'small' | 'sm' | 'lg' | 'large' | 'md' | 'medium'
		// Custom props
		link?: string
		copy?: string
	}>
>()

const clicked = ref<boolean>(false)
const disabled = computed(() => clicked.value || props.disabled || props.args.disabled)

function onRenderEvent(_event: Event): void
{
	if (clicked.value)
	{
		clicked.value = false
		Streamlit.setComponentValue(clicked.value)
	}
}

onMounted(() =>
	{
		Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
	})

onUnmounted(() =>
	{
		Streamlit.events.removeEventListener(Streamlit.RENDER_EVENT, onRenderEvent)
	})

async function onClick()
{
	if (clicked.value)
	{
		clicked.value = false
		Streamlit.setComponentValue(clicked.value)

		await new Promise(resolve => setTimeout(resolve, 50))
	}

	clicked.value = true
	Streamlit.setComponentValue(clicked.value)
}
</script>

<template>
	<div class="component" :style="style">
		<DsfrButton
			v-bind="props.args"
			:disabled="disabled"
			@click="onClick"
		/>
	</div>
</template>
